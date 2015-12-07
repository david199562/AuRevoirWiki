## Au revoir, Wiki.

![phase-design-orange](https://img.shields.io/badge/phase-design-orange.svg)

### How it works:
1. Client logs in (i.e. gain access to gist API), sends request (e.g. "Machine Learning") to the request gist (format=JSON). Client also creates a content gist.
2. "Pseudo-Server" reads the request gist periodically and process the searching and downloading, then update the corresponding content gist.
3. Client fetch content gist.

### Why it works:
Gist supports 5000 API requests per hour for registered accounts. Should satisfy a small number of users. If the user also has an account, the scalability of this service and **its potential risk** will both rise.
