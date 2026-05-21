module.exports = {
  run: [
    {
      method: "shell.run",
      params: {
        message: {
          _: ["git", "pull"]
        }
      }
    },
    {
      method: "shell.run",
      params: {
        path: "app",
        message: {
          _: ["git", "pull"]
        }
      }
    },
    {
      method: "shell.run",
      params: {
        venv: "env",
        path: "app",
        message: {
          _: ["uv", "sync", "--extra", "ui", "--active"]
        }
      }
    }
  ]
}
