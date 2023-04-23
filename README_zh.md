<h1 align="center">
    cWebDXCE
</h1>

<p align="center">
  <a href="/README.md">English</a> |
  <a href="">Demo</a> |
  <a href="https://vercel.com/new/clone?repository-url=https://github.com/HsiangNianian/cWebDXCE" target="_blank">Deploy</a>
</p>

该Github仓库是一个包含前端和后端文件夹的骰子应用程序，使用了 Vue.js、axios 和 Flask 等技术栈来实现 CRUD 操作。用户可以在页面上输入一个骰子的名称和面数并将其添加到列表中。每个骰子都有其独特的 ID，在用户点击删除或掷骰子按钮时可以使用它。

仓库结构
-------

- frontend：前端文件夹，包含了基于 Vue.js 和 axios 实现的前端骰子应用程序。
  - `index.html`：前端应用程序的 HTML 文件。
- backend：后端文件夹，包含了使用 Flask 框架实现的后端 API 接口和数据库操作。
  - `app.py`：基于 Flask 框架实现的 Python 应用程序，提供了 CRUD 操作的 API 接口。
  - `database`：数据库文件夹，存放了 `dice.db` 数据库文件。

API 接口
--------

- `GET /api/dice`：获取所有骰子信息。
- `POST /api/dice`：新增一个骰子信息。
- `DELETE /api/dice/<int:id>`：删除指定 ID 的骰子。
- `GET /api/roll/<int:id>`：投掷指定 ID 的骰子并返回结果。

应用程序连接了 `database/dice.db` 数据库，并创建了 `Dice` 表，用于存储骰子信息。`Dice` 表包含 `id`, `name`, `sides`, 和 `created_at` 四个字段。

说明
----

该仓库使用了 Axios 库来处理 HTTP 请求和响应，以及 Node.js 和 Express 框架构建了一个简单的 RESTful API，用于执行 CRUD 操作。

通过该仓库，开发者可以学习到如何使用 Vue.js、Axios 和 Flask 等技术栈创建 Web 应用程序，包括如何进行 HTTP 通信并处理响应。此外，还可以学习到如何使用 Express 框架构建 RESTful API 以实现 CRUD 操作，这是 Web 应用程序中常见的功能。

贡献者
-----

<a href="https://github.com/HsiangNianian/cWebDXCE/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HsiangNianian/cWebDXCE" />
</a>

License
-------

[MIT](https://github.com/HsiangNianian/cWebDXCE/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
