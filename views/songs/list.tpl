% include('header.tpl')
<h1 class="text-center">View Song Results</h1>
<div class="table-responsive">
  <table class="table table-hover">
    <thead>
      <tr>
        <th>Title</th>
        <th>Production Year</th>
        <th>CD</th>
        <th>Singer</th>
        <th>Songwriter</th>
        <th>Composer</th>
        <th>Edit?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Back to Black</td>
        <td>2007</td>
        <td>Back to Black</td>
        <td>Amy Winehouse</td>
        <td>Amy Winehouse</td>
        <td>Mark Ronson</td>
        <td>
          <a class="btn btn-default" href="songs/Back+to+Black" role="button">
            Edit Me!
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
% include('footer.tpl')
