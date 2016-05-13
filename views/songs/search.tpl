% include('header.tpl')
<h1 class="text-center">Presentation of Songs</h1>
<form class="form-horizontal" action="songs/search" method="post">
  <div class="form-group">
    <label for="title" class="col-sm-2 control-label">Title</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="title" id="title" />
    </div>
  </div>
  <div class="form-group">
    <label for="year" class="col-sm-2 control-label">Production Year</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="year" id="year"/>
    </div>
  </div>
  <div class="form-group">
    <label for="company" class="col-sm-2 control-label">Company</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="company" id="company" />
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>

%if results:
<h2 class="text-center">View Song Results</h2>
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
        <td>12</td>
        <td>1234</td>
        <td>5678</td>
        <td>9123</td>
        <td>
          <a class="btn btn-default" href="songs/Back+to+Black" role="button">
            Edit Me!
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
%end
% include('footer.tpl')
