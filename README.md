# conundrum

### A webframework agnostic blogging plugin in Python

The idea is pretty simple. To make a create post -

  - Fetch a public gist* from github, with a markdown file
  - Save as markdown text in a yaml file with other info like date
  - Keep a file with the name of the newest post
  - Maintain an archive

And to display -

  - Archive is returned as html
  - Blog post is returned as html if name is given, else the newest post is returned

*For now it is possible to fetch post only from public gists. Support for more services will be added later.

## Usage -

  - Make sure you have a folder named **posts** in your application directory.
  - Create a public gist in markdown format as your post
  - Call from your application `conundrum.fetch(gist_id, name/title, github_username)
    - It will fetch the gist and save it in a yaml file named <title>, along with some other data
    - It will also update the archive, which is saved as a markdown file in the **posts** directory
    - And it will update a file named **first** with the name of the new file.
  - To update a post, call `conundrum.update(title)` and it will update the post.
  - To get the archive, call `conundrum.archive()`
  - To get a post call `conundrum.blog(title)`.
    - It will return the html of that particular blog post, if it exists.
    - If no title is supplied, it will return the latest post.
  - A function `operate` is provided. It will take in arguments, and send them as `post` data to a url in the args
    - The format is `conundrum.operate(-p|-u url title <gist_id> <auth>)`
      - -p for post, -u for update(not used right now, but will be later)
      - `url` is the url you want to call on your site. Eg domain.tld/fetch to create a post, domain.tld/update to update it
      - `title` is the title of the post
      - `gist_id` is required only when you're creating a new post
      - `auth` is optional, you can use it to send authentication
    - This function is pretty basic, and it would be much better, and easier to create one of your own

## To Do

  - Make it possible for the user to change the posts directory
  - Add support for private gists, and more services(dropbox, google drive...)
