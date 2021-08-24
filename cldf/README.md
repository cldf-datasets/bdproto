<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset bdproto

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Marsico, Egidio, Sebastien Flavier, Annemarie Verkerk and Steven Moran. 2018. BDPROTO: A Database of Phonological Inventories from Ancient and Reconstructed Languages. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), 1654-1658. May 7-12, Miyazaki, Japan. Online: http://www.lrec-conf.org/proceedings/lrec2018/pdf/534.pdf.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://github.com/bdproto/bdproto
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | git@github.com:cldf-datasets/bdproto
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="git@github.com:cldf-datasets/bdproto/tree/a109e4a">git@github.com:cldf-datasets/bdproto a109e4a</a></li><li><a href="git@github.com:glottolog/glottolog/tree/f6531fcec3">Glottolog v4.4-20-gf6531fcec3</a></li><li><a href="https://github.com/bdproto/bdproto/tree/d201acb">bdproto/bdproto v1.1-15-gd201acb</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.11</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | bdproto
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-valuescsv"></a>Table [values.csv](./values.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 7880


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Inventory_ID](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | `string` | References [contributions.csv::ID](#table-contributionscsv)
`SourceLanguageName` | `string` | 
`SourceLanguageFamily` | `string` | 
`PhonemeNotes` | `string` | 
`PhonemeNFD` | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 7880


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 214


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
`family_id` | `string` | 
`parent_id` | `string` | 
`bookkeeping` | `string` | 
`level` | `string` | 
`description` | `string` | 
`markup_description` | `string` | 
`child_family_count` | `string` | 
`child_language_count` | `string` | 
`child_dialect_count` | `string` | 
`country_ids` | `string` | 

## <a name="table-contributionscsv"></a>Table [contributions.csv](./contributions.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 272


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Allophone` | `string` | 
`AllophoneNotes` | `string` | 
`SpecificDialect` | `string` | 
`Variants` | `string` | 
`LowconfidencePhonemic` | `string` | 
`LowconfidencePhonetic` | `string` | 
`LanguageName` | `string` | 
`LanguageFamily` | `string` | 
`LanguageFamilyRoot` | `string` | 
`Glottocode` | `string` | 
`Type` | `string` | 
`Macroarea` | `string` | 
`Dates` | `string` | 
`DatesSource` | `string` | 
`InventoryType` | `string` | 
`TimeDepth` | `string` | 
`TimeDepthYBP` | `string` | 
`Homeland` | `string` | 
`HomelandSource` | `string` | 
`BibtexKey` | `string` | 
`Source` | `string` | 
`Comments` | `string` | 

