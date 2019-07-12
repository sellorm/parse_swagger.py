# parse_swagger

A quick tool to parse swagger/openapi json files for printing to the console.

This is especially useful for static reporting where sending the json would not be appropriate for your audience.

```
./parse_swagger.py <filename.json>
```

The output looks a bit like this:

```
Path: /compare_inputs/{input1}/{input2}
Method: get
Summary: Fetch the result of a variant comparisson.
OperationId: compareInputs

Parameters: {'name': 'input1', 'in': 'path', 'description': 'The first input.', 'required': True}
Parameters: {'name': 'input2', 'in': 'path', 'description': 'The second input.', 'required': True}
RequestBody: None
Response: 200 - OK.
Response: 400 - Bad Request.
Response: 404 - NotFound.
Response: 500 - Internal Server Error.
Response: 503 - Service Unavailable.
```
