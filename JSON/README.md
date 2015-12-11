### Request Format

```
{
  "pat": "e2aa05f18d9fb",      // PAT for API access
  "reqs": [                    // List of requests
    {
      "keyword": "cespedia",   // Search keyword
      "inc_pic": true,         // Include picture content
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
  "availability": 256,         // IMPORTANT. Availability of this PAT
                               // 
                               // API access for each request = 8
                               // EDIT   request list,
                               // CREATE txt cahce
                               // CREATE pic cache
                               // READ   request list
                               // EDIT   txt cache
                               // EDIT   pic cache
                               // READ   txt cache
                               // READ   pic cache
                               // 
                               // 5000 / 8 = 625
                               // I don't want to be found abusing the API
                               // so let's limit the availability to
                               // 300 requests per hour for now.

  "req_count": 6,              // Lifetime sum of requests of this PAT
  "last_active": "201505:0Z"   // Time of last request in ISO 8601 format:
}                              // 2015-12-05T13:11:59Z
                               // T indicates start of time element
                               // Z indicates zero UTC offset
```