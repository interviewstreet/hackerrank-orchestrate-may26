---
title: "Configurations for Front-end, Back-end and Full stack Developer Questions"
title_slug: "configurations-for-front-end-back-end-and-full-stack-developer-questions"
source_url: "https://support.hackerrank.com/articles/9443018671-configurations-for-front-end%2C-back-end-and-full-stack-developer-questions"
article_slug: "9443018671-configurations-for-front-end%2C-back-end-and-full-stack-developer-questions"
last_updated_exact: "Dec 13, 2024, 5:13 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Project Questions"
---

# Configurations for Front-end, Back-end and Full stack Developer Questions

_Last updated: Dec 13, 2024, 5:13 AM (Last updated 1 year ago)_

A valid project should have a valid **hackerrank.yml** configuration file in the root directory. Refer to the examples below or the configuration reference to learn how to write one for your project. 

## **Configuration Reference**

```
version: (number)- [required] Version number for the configuration schema.
  - Current version is 1.0configuration: (hash)- [required] Parent attribute for the configuration.
  - All project configurations are provided herehas_webserver: (boolean)
    - [required] Define if a project has an exposed web server
      (can be accessed outside of the server).
    - Use open port (3000, 3030, 5000, 6000, 6001, 8000, 8080) 
      for publishing the server. All other ports are blocked out outside communication.
  readonly_paths: (array)
    - [optional] A list of file paths and/or regex patterns 
      that should be marked read-only for candidates
  scoring: [optional] (hash)
    - [required] Parent attribute for scoring related configuration
    command: (string)
      - [required] Scoring command is defined here. 
      - This attribute must be provided for scoring to work
    files: (array)
      - [optional] A list of scoring output files can be provided here.
      - Once the scoring command is run, the platform will search for these files 
        and parse them to calculate the final score.
      - If these files are not provided, the scoring command output is used for scoring.
    testcase_weights: (hash [<testcase name>:<weight>])
      - [optional] This attribute can be used to provide weighted scoring 
        for test cases.
      - The sum total of all weights should be 
        1. Validation will fail if the sum total of all weights is not one.
      - The test case weights are matched by test case name, 
        so all test case names should be unique (across files).
  ide_config: (hash)
    - [required] All IDE related configuration is provided here
    default_open_files: (array)
      - [required] Provide a list of default files to open here. 
        Path should be relative to project root folder.
    project_menu: (string)
      - [required] Define project menu commands here. All child attributes are required.
      run:
        - [required] Provide command for Project > Run menu item
      install:
        - [required] Provide command for Project > Install menu item
      test:
        - [required] Provide command for Project > Test menu item
```

## Example 1: Sample config for a node project without scoring

```
version: 1.0configuration:has_webserver: falseide_config:
    default_open_files:
      - app.js
    project_menu: 
      run: npm start
      install: npm install
      test: npm test
```

## Example 2: Sample config for a node project with a web server and scoring

```
version: 1.0configuration:has_webserver: truescoring:
    # npm test is expected to produce test output in results/unit.xml file.
    command: "npm test"
    files:
      - results/unit.xmlide_config:
    default_open_files:
      - app.js
    project_menu: 
      run: npm start
      install: npm install
      test: npm test
```

## Example 3: Sample config for a Java Spring Boot API project with weighted test cases

```
version: 1.0configuration:has_webserver: falsescoring:
    command: "mvn clean test"
    files:
      - target/customReports/result.xml
    testcase_weights:
      # The weights should sum up to a total of 1
      Create a model: 0.2
      Delete a model: 0.2
      Edit a model: 0.2
      Filter model by attribute: 0.4ide_config:
    default_open_files:
      - src/main/java/com/hackerrank/sample/controller/ModelController.java
      - src/main/java/com/hackerrank/sample/model/Model.java
    project_menu: 
      run: mvn clean spring-boot:run
      install: mvn clean install
      test: mvn clean test; cat target/customReports/result.txt
```

## Example 4: Sample config for a node project with a web server and multiple output files

```
version: 1.0configuration:has_webserver: truescoring:
    # npm test is expected to produce test output in results/unit.xml file.
    command: "npm test"
    files:
      - results/user.xml
      - results/project.xml
      - results/api.xmlide_config:
    default_open_files:
      - app.js
    project_menu: 
      run: npm start
      install: npm install
      test: npm test
```

## Example 5: Sample config for a node project with read-only files

You can use read-only files to mark certain files like test cases read-only. The candidate will not be able to modify these files.

```
version: 1.0configuration:has_webserver: true
  readonly_paths:
    - app/test.js
    - app/tests/*scoring:
    command: "npm test"
    files:
      - results/unit.xmlide_config:
    default_open_files:
      - app.js
    project_menu:
      run: npm start
      install: npm install
      test: npm test
```

\
