# Au revoir, Wiki. BETA VERSION

### TODO
Todos are at **Issues** and are green tagged "help needed". There is also a Milestone for the beta release.

We will use private gists so the only way to access them is through IDs. The IDs are stored in variables at runtime. So encryption of the content may not be necessary at this point. However, compression is always paramount because content larger than 1MB will be [truncated according to the API](https://developer.github.com/v3/gists/#truncation). And that's also why we need a text cache and dedicated picture caches.

### Repo Structure
- **FrontEnd:** the web page.
- **JSON:** frontend-backend communication interfaces.
- **Tools:** algorithm implementations and convenience libraries.

### External Libraries
Edit the list when you decide to add more.

-[Wikipedia API Python Wrapper](https://github.com/goldsmith/Wikipedia). Very, very convenient.
-[WiTeX](https://github.com/AndrewBelt/WiTeX). Actually pretty useful for figuring out the page layout.
