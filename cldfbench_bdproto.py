import pathlib
import subprocess
import unicodedata
import hashlib
from cldfbench import Dataset as BaseDataset
from cldfbench import CLDFSpec


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "bdproto"
    # valueTableProperties = ['SourceLanguageName', 'SourceLanguageFamily', 'PhonemeNotes', 'PhonemeNFD']
    valueTableProperties = ['PhonemeNotes', 'PhonemeNFD']
    # languageTableProperties = ['family_id', 'parent_id', 'bookkeeping', 'level', 'description', 'markup_description', 'child_family_count', 'child_language_count', 'child_dialect_count', 'country_ids']
    languageTableProperties = ['family_id', 'parent_id', 'bookkeeping', 'level', 'description', 'markup_description', 'child_family_count', 'child_language_count', 'child_dialect_count', 'country_ids']
    languageTableProperties_additional = ['LanguageFamily', 'LanguageFamilyRoot', 'Macroarea']
    # inventoryTableProperties = ['SpecificDialect', 'LanguageName', 'LanguageFamily', 'LanguageFamilyRoot', 'Glottocode', 'Type', 'Macroarea', 'Dates', 'DatesSource', 'InventoryType', 'TimeDepth', 'TimeDepthYBP', 'Homeland', 'HomelandSource', 'BibtexKey', 'Source', 'Comments']
    inventoryTableProperties = ['SourceLanguageName', 'SourceLanguageFamily', 'SpecificDialect', 'Glottocode', 'Type', 'Dates', 'DatesSource', 'InventoryType', 'TimeDepth', 'TimeDepthYBP', 'HomelandLatitude', 'HomelandLongitude', 'HomelandSource', 'HomelandComments', 'BibtexKey', 'Source', 'Comments']
    

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(dir=self.cldf_dir, module='StructureDataset')

    def cmd_download(self, args):
        subprocess.check_call(
            'git -C {} submodule update --remote'.format(self.dir.resolve()), shell=True)

    def create_schema(self, ds):
        # values.csv
        ds.remove_columns('ValueTable', 'Code_ID', 'Comment', 'Source')
        ds.add_columns(
            'ValueTable',
            {
                "dc:extent": "singlevalued",
                "datatype": "string",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#contributionReference",
                "required": True,
                "name": "Inventory_ID"
            },
            *self.valueTableProperties,
        )

        # parameters.csv
        ds.add_component('ParameterTable')

        # languages.csv
        ds.add_component('LanguageTable')
        ds.remove_columns('LanguageTable', 'Macroarea')
        ds.add_columns('LanguageTable', *self.languageTableProperties_additional)
        ds.add_columns('LanguageTable', *self.languageTableProperties)

        # contributions.csv
        ds.add_component('ContributionTable')
        ds.remove_columns('ContributionTable', 'Name', 'Description', 'Contributor', 'Citation')
        ds.add_columns(
            'ContributionTable',
            *self.inventoryTableProperties,
        )
        ds.add_foreign_key('ValueTable', 'Inventory_ID', 'ContributionTable', 'ID')

    def cmd_makecldf(self, args):
        self.create_schema(args.writer.cldf)

        counter = 1
        inventory_ids = []
        pids = []
        language_map = {}
        for row in self.raw_dir.read_csv(
            self.raw_dir / 'bdproto' / 'bdproto.csv',
            dicts=True,
        ):
            desc = ' - '.join(unicodedata.name(c) for c in row['Phoneme'])
            pid = hashlib.md5(desc.encode('utf8')).hexdigest().upper()

            # values.csv
            args.writer.objects['ValueTable'].append({
                'ID': str(counter),
                'Inventory_ID': row['BdprotoID'],
                'Language_ID': row['Glottocode'] if row['Glottocode'] != 'NA' else '',
                'Parameter_ID': pid,
                'Value': row['Phoneme'],
                **{ k: row[k] for k in self.valueTableProperties}
            })

            # parameters.csv
            if pid not in pids:
                args.writer.objects['ParameterTable'].append({
                    'ID': pid,
                    'Name': row['Phoneme'],
                    'Description': desc, 
                })
                pids.append(pid)

            # contributions.csv
            if row['BdprotoID'] not in inventory_ids:
                args.writer.objects['ContributionTable'].append({
                    'ID': row['BdprotoID'],
                    **{ k: row[k] for k in self.inventoryTableProperties}
                })
                inventory_ids.append(row['BdprotoID'])

            counter += 1

            if row['Glottocode'] != 'NA':
                language_map[row['Glottocode']] = {k: row[k] for k in self.languageTableProperties_additional}

        # languages.csv
        language_ids = list(map(lambda row: row['Language_ID'], args.writer.objects['ValueTable']))
        language_ids = list(dict.fromkeys(language_ids))
        for row in self.raw_dir.read_csv(
            self.raw_dir / 'bdproto' / 'src' / 'glottolog_languoid.csv' / 'languoid.csv',
            dicts=True,
        ):
            if row['id'] in language_ids:
                args.writer.objects['LanguageTable'].append({
                    'ID': row['id'],
                    'Name': row['name'],
                    'Glottocode': row['id'],
                    'ISO639P3code': row['iso639P3code'],
                    'Latitude': row['latitude'],
                    'Longitude': row['longitude'],
                    **language_map[row['id']],
                    **{ k: row[k] for k in self.languageTableProperties}
                })
        
