# Reports

The primary functionality of the app is the ability to send and receive reports.

## TODOs

- Complete schema for individual report
- Implement

## Required endpoints

**GET** `/reports/:patientID/most-recent` - Retrieves a patient's most recent report.

Request body:

```json
{
  patientID: <str>,
  sessionID: <str>
}
```

Response:

```json
{
  reportID: <str>
  ...
}
```

**GET** `/reports/:patientID` - Retrieves all of a patient's reports.

Request body:

```json
{
  patientID: <str>,
  sessionID: <str>
}
```

Response:

```json
{
  reports: [
    {
      reportID: <str>
      ...
    }, ... , {
      reportID: <str>
      ...
    }
  ]
}
```

**POST** `/reports/:patientID` - Creates a new report for that patientID.

Request body:

```json
{
  patientID: <str>,
  sessionID: <str>
}
```

Response:

```json
{
  reportID: <str> #ID of newly created report
  ...
}
```

**PUT** `/reports/:patientID/:reportID`

Request body:

```json
{
  patientID: <str>, #required
  sessionID: <str>, #required
  ... #all other fields optional, select from schema
}
```

Response:

```json
{
  reportID: <str>
  ...
}
```
