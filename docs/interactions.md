# Interactions

A major goal of the prototype is the ability to track users' interactions with the app.

## TODOs

- Server-side authentication to enable a session ID for use in POST. This will allow us to track individual users across devices/apps.

## Required endpoints

**POST** `/interactions/:mID`

Request body:

```json
{
  source: <str>,
  time: <str>,
  type: enum <str> {keystroke, button},
  sessionID: <str>
}
```

Response:

```json
{}
```
