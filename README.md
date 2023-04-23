<h1 align="center">
    cWebDXCE
</h1>

<p align="center">
  <a href="/README_zh.md">简体中文</a>
  <a href="">Demo</a>
  <a href="https://vercel.com/new/clone?repository-url=https://github.com/HsiangNianian/cWebDXCE" target="_blank">Deploy</a>
</p>

This Github repository is a dice application that includes both frontend and backend folders, using technology stacks such as Vue.js, axios, and Flask to achieve CRUD operations. Users can enter the name and number of faces of a dice on the page and add it to the list. Each dice has its unique ID, which can be used when the user clicks the delete or roll button.

Repository Structure
-------

- frontend: The frontend folder contains the frontend dice application implemented based on Vue.js and Axios.
  - `index.html`: The HTML file of the frontend application.
- backend: The backend folder contains the backend API interface and database operation implemented using the Flask framework.
  - `app.py`: A Python application implemented based on the Flask framework, which provides CRUD operation API interfaces.
  - `database`: The database folder contains the `dice.db` database file.

API Interface
--------

- `GET /api/dice`: Get information for all dice.
- `POST /api/dice`: Add information for a new dice.
- `DELETE /api/dice/<int:id>`: Delete the specified ID dice.
- `GET /api/roll/<int:id>`: Roll the specified ID dice and return the result.

The application connects to the `database/dice.db` database and creates a `Dice` table to store dice information. The `Dice` table contains four fields: `id`, `name`, `sides`, and `created_at`.

Description
----

This repository uses the Axios library to handle HTTP requests and responses, and builds a simple RESTful API using Node.js and the Express framework to perform CRUD operations.

Through this repository, developers can learn how to create web applications using technology stacks such as Vue.js, Axios, and Flask, including how to communicate via HTTP and handle responses. In addition, you can also learn how to use the Express framework to build RESTful APIs to achieve CRUD operations, which are common functions in web applications.

Contributors
-----

<a href="https://github.com/HsiangNianian/cWebDXCE/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HsiangNianian/cWebDXCE" />
</a>

License
-------

[MIT](https://github.com/HsiangNianian/cWebDXCE/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)