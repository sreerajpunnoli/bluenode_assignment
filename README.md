# bluenode_assignment
This repositoy is for the development of bluenode data parsing system. It uses python to parse the input file using error_codes.json and standard_definition.json files in the inputs directory. More about the task can be found in TASK_OBJECTIVE.md

Installation
------------


    $ pip install -r requirements.txt



Modules
-------

1. inputs: Default input files are added in the module

	* error_codes.json : Default error code definition file
	* standard_definition.json : Default standard definition file
	* input_file.txt : : Default input file

2. config: Configuration module

	* settings.yml : The location of the files and dictioanry keys can be modified using this yaml file. This will override the default configs. Edit and uncomment the fileds which needs to be modified.

3. bluenode: Utils module

	* load_settings.py
	* extract_input_files_data.py
	* parse_data.py
	* extract_fields.py
	* write_results.py

4. parsed: Parsed results are stored in the module

	* report.csv
	* summary.txt

5. tests: Unit tests are included in the module

	* test_parse.py : Tests the summary output and the report output


Running
-------

Default input files are stored in inputs directory. The settings.yml file in config directory can be used to specify different input files and output files location. Once the files are specified properly, use the below command to start parsing the input file


    $ python parse_bluenode_data.py



Unit Tests
----------

Unit tests tests the parsing process. It checks whether the summary and eport are created as per requirement. Unit tests can be run using the following command.


    $ python -m tests.test_parse