
# Museum API

Museum API allows you to easily fetch data from the museum api through python objects without needing you to send requests to its api endpoints using requests module.


## Installation

Install MuseumAPI package for fetching data from Museum API and converting that data to different formats using:

```bash
  pip install MuseumAPI-yogeshwar
```
    
# Usage

```pythonscript
from Museum_API.museum import MuseumAPI
from Museum_API.converters import Converter, flatten
m=MuseumAPI()
```


## Usage examples:
To fetch all the object ids of all the objects available on Museum API:
```pythonscript
# fetches all the object ids from Museum API.
object_ids = m.get_all_object_ids()
```
This will return:
```pythonscript
    {
	"total": 471581,
	"objectIDs": [
		1,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9,
		10,
		// more results ...
	]
}
```
To fetch the details of an object for particular object id:
```pythonscript
# fetches all the object ids from Museum API.
object_data = m.get_object_for_id(1)
```
This will return object from Museum API which have objectId as 1.

To convert Json data to CSV,PDF,HTML,Excel,XML use functions of Converter class:
```pythonscript
Converter.convert_to_csv(object_list, os.path.join(files_dir, "museum_csv.csv"))
Converter.convert_to_pdf(object_list, os.path.join(files_dir, "museum_pdf.pdf"))
Converter.convert_to_html(object_list, os.path.join(files_dir, "museum_html.html"))
Converter.convert_to_xml(object_list, os.path.join(files_dir, "museum_xml.xml"))
Converter.convert_to_excel(object_list, os.path.join(files_dir, "museum_excel.xlsx"))
```
## License

[MIT](https://github.com/yogeshwarreddy13/Museum-codeops/blob/master/LICENSE)

