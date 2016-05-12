% include('header.tpl')
<h1 class="text-center">View Artist Results</h1>
<div class="table-responsive">
  <table class="table table-hover">
    <thead>
      <tr>
        <th>National ID</th>
        <th>Name</th>
        <th>Surname</th>
        <th>Birth Year</th>
        <th>Edit?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1234</td>
        <td>Mario</td>
        <td>Saldinger</td>
        <td>1996</td>
        <td>
          <a class="btn btn-default" href="artists/1234" role="button">
            Edit Me!
          </a>
        </td>
      </tr>
      <tr>
        <td>1235</td>
        <td>Alexandros</td>
        <td>Kalimeris</td>
        <td>1996</td>
        <td>
          <a class="btn btn-default" href="artists/1235" role="button">
            Edit Me!
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
% include('footer.tpl')
