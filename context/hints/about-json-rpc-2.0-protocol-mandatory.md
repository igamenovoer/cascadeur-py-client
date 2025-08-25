# JSON-RPC 2.0 Protocol: Mandatory Requirements for Hand-Crafted Messages

Sources:
- JSON-RPC 2.0 Specification: https://www.jsonrpc.org/specification

Scope
- This guide enumerates the MUST/SHALL requirements of JSON‑RPC 2.0 so you can craft conformant messages by hand. JSON‑RPC is transport‑agnostic; boundaries are handled by your transport (e.g., length‑prefix over pipes).

Notation
- “MUST”, “SHOULD”, etc. are per RFC 2119.
- Member names are case‑sensitive (per spec “Conventions”).

Request Object (client → server)
A Request is a JSON Object with these members:
- jsonrpc: MUST be the String "2.0".
- method: MUST be a String. Names beginning with "rpc." are RESERVED and MUST NOT be used for application methods.
- params: MAY be omitted. If present, MUST be either:
  - Array (by‑position), or
  - Object (by‑name) with names that MUST match the server’s parameter names exactly (including case).
- id: If included, MUST be String | Number | Null. If omitted, the Request is a Notification. Numbers SHOULD NOT contain fractional parts. Using Null is DISCOURAGED.

Examples (valid Requests)
```json
{"jsonrpc":"2.0","method":"subtract","params":[42,23],"id":1}
```
```json
{"jsonrpc":"2.0","method":"subtract","params":{"minuend":42,"subtrahend":23},"id":"abc"}
```

Notification (no response)
- A Request without id is a Notification. The server MUST NOT send a Response.
```json
{"jsonrpc":"2.0","method":"update","params":[1,2,3]}
```

Response Object (server → client)
A Response is a JSON Object with these members:
- jsonrpc: MUST be the String "2.0".
- result: REQUIRED on success. MUST NOT exist if error is present.
- error: REQUIRED on error. MUST NOT exist if result is present. See Error object below.
- id: REQUIRED. MUST be identical to the Request’s id. If the Request id could not be determined (e.g., parse/invalid request), id MUST be Null.

Examples (valid Responses)
Success:
```json
{"jsonrpc":"2.0","result":19,"id":1}
```
Error:
```json
{"jsonrpc":"2.0","error":{"code":-32601,"message":"Method not found"},"id":"abc"}
```

Error Object (in Response.error)
- code: REQUIRED Number (integer). Reserved range −32768..−32000 for standard errors.
- message: REQUIRED String. Concise, single sentence.
- data: OPTIONAL (any JSON value) with additional info.

Standard error codes
- -32700 Parse error — invalid JSON received.
- -32600 Invalid Request — JSON is not a valid Request object.
- -32601 Method not found — method does not exist / not available.
- -32602 Invalid params — invalid method parameter(s).
- -32603 Internal error — internal JSON‑RPC error.
- -32000 to -32099 Server error — reserved for implementation‑defined server errors.

Batch Requests
- Client MAY send an Array of Request objects.
- Server SHOULD respond with an Array of Response objects (order arbitrary).
- For Notifications within the batch, the server MUST NOT include any Response.
- An empty Array is INVALID; respond with a single error Response (-32600, id: null).
- If the batch itself is not valid JSON or not an Array with ≥1 value, respond with a single error Response.

Example (batch of mixed requests)
```json
[
  {"jsonrpc":"2.0","method":"sum","params":[1,2,4],"id":"1"},
  {"jsonrpc":"2.0","method":"notify_hello","params":[7]},
  {"jsonrpc":"2.0","method":"subtract","params":[42,23],"id":"2"}
]
```
Possible Response:
```json
[
  {"jsonrpc":"2.0","result":7,"id":"1"},
  {"jsonrpc":"2.0","result":19,"id":"2"}
]
```

Validation Checklists
Client‑side (before sending Request)
- Ensure jsonrpc == "2.0".
- Ensure method is non‑empty String and not starting with "rpc.".
- If params present: Array or Object (correct names/case when by‑name).
- If id present: String | Number (no fractional) | Null.

Server‑side (when creating Response)
- Echo the request id exactly; use null only when request id cannot be determined (parse/invalid request).
- Include exactly one of result or error (never both, never neither).
- On success: include result; omit error.
- On error: include error object with integer code and message; optionally data; omit result.
- For Notifications: do not send any Response.

Interop Notes
- Additional, non‑standard members in Request/Response are permitted by many implementations and typically ignored, but are not part of the core spec; avoid relying on them for interoperability.
- Member names are case‑sensitive; keep exact casing.
- Transport framing is out of scope. If you are using byte streams (e.g., Windows named pipes), add a message boundary (e.g., 4‑byte length prefix) or use a message‑oriented transport.

Minimal JSON Schemas (for quick validation)
Request (simplified; either result or error not expressed here):
```json
{
  "type":"object",
  "required":["jsonrpc","method"],
  "properties":{
    "jsonrpc":{"const":"2.0"},
    "method":{"type":"string"},
    "params":{
      "oneOf":[{"type":"array"},{"type":"object"}]
    },
    "id":{
      "oneOf":[
        {"type":"string"},
        {"type":"integer"},
        {"type":"number","multipleOf":1},
        {"type":"null"}
      ]
    }
  },
  "additionalProperties":true
}
```
Response (success):
```json
{
  "type":"object",
  "required":["jsonrpc","result","id"],
  "not":{"required":["error"]},
  "properties":{
    "jsonrpc":{"const":"2.0"},
    "result":{},
    "id":{}
  },
  "additionalProperties":true
}
```
Response (error):
```json
{
  "type":"object",
  "required":["jsonrpc","error","id"],
  "not":{"required":["result"]},
  "properties":{
    "jsonrpc":{"const":"2.0"},
    "error":{
      "type":"object",
      "required":["code","message"],
      "properties":{
        "code":{"type":"integer"},
        "message":{"type":"string"},
        "data":{}
      }
    },
    "id":{}
  },
  "additionalProperties":true
}
```

Quick Compliance Pitfalls
- Forgetting jsonrpc:"2.0".
- Returning both result and error (disallowed).
- Sending a Response to a Notification (disallowed).
- Not echoing the request id exactly; using non‑null id for parse/invalid request errors (must be null).
- Using fractional Number for id (SHOULD NOT).
- Using "rpc.*" for application method names (reserved).

See also
- JSON-RPC 2.0 spec: https://www.jsonrpc.org/specification
- Framing and IPC notes: see local hint [about-single-machine-server-client-ipc.md](./about-single-machine-server-client-ipc.md)