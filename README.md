<h1 align="center">
    cWebDXCE
</h1>

<p align="center">
  <a href="/README_zh.md">简体中文</a> |
  <a href="">Demo</a> |
  <a href="https://vercel.com/new/clone?repository-url=https://github.com/HsiangNianian/cWebDXCE" target="_blank">Deploy</a>
</p>

This repository contains a TTRPG dice Web app. It includes an user interface which has adopted Vue.js, axios, and Flask to enable CRUD operations. Users can add a dice instance to the dice list by entering the name and number of faces of a dice on the page. Each dice has its unique ID for operations such as roll, deletion, etc.

Repository Structure
-------

- frontend: The frontend folder containing the frontend dice application powered by Vue.js and Axios.
  - `index.html`: The frontend entry page.
- backend: The backend folder handling the interface and database operation, implemented using the Flask framework.
  - `app.py`: A Python application implemented with Flask which provides CRUD-operational APIs.
  - `database`: The database folder with the `dice.db` database file.

Interface
--------

- `GET /api/dice`: Get information for all dice.
- `POST /api/dice`: Add a new dice.
- `DELETE /api/dice/<int:id>`: Delete dice by ID.
- `GET /api/roll/<int:id>`: Roll a dice specified by ID.

The application creates a `Dice` table in `database/dice.db` to store dice information. The table has four fields: `id`, `name`, `sides`, and `created_at`.

Description
----

This application uses the Axios library to handle HTTP requests and responses, and builds a simple RESTful API using Node.js and the Express framework to perform CRUD operations.

This repository can be an example of how to create web applications using technology stacks like Vue.js, Axios, and Flask, and additionally, how to implement frontend--backend communication via HTTP and handle responses. It also features the use of Express framework to build RESTful APIs to achieve CRUD operations, which are common functions in web applications.

Contributors
-----

<a href="https://github.com/HsiangNianian/cWebDXCE/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HsiangNianian/cWebDXCE" />
</a>

License
-------

[MIT](https://github.com/HsiangNianian/cWebDXCE/blob/master/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
