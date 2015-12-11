### Request Format

```JSON
{
  "access": "e2aa05f18d9fb",   // PAT for caches
  "reqs": [                    // List of requests
    {
      "keyword": "cespedia",   // Search keyword
      "inc_pic": true,             // Include picture content
      "txt_cache": "42b5ca",   // Cache ID
      "pic_cache": [...]       // List of cache IDs
    },
    {
      "keyword": "mace ing",
      "inc_pic": false,
      "txt_cache": "42dcb1",
      "pic_cache": null
    }
  ],
  "availability": 698,         // Availability of this PAT
  "req_count": 6,                  // Lifetime sum of requests of this PAT
  "last_active": "201505:0Z"   // Time of last request in ISO 8601 format:
}                              // 2015-12-05T13:11:59Z
                               // T indicates start of time element
                               // Z indicates zero UTC offset
```