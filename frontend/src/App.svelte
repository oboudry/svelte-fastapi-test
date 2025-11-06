<script>
  let message = "Loading..."
  fetch("http://127.0.0.1:8000/api/hello")
    .then(r => r.json())
    .then(data => message = data.message)
</script>

<main>
  <h1>{message}</h1>
</main>

<style>
  main {
    text-align: center;
    padding-top: 4rem;
    font-family: sans-serif;
  }
</style>

