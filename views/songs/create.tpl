% include('header.tpl')
<h1 class="text-center">Insert Song</h1>
<form class="form-horizontal" action="songs/create" method="post">
  <div class="form-group">
    <label for="title" class="col-sm-2 control-label">Title</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="title" id="title" />
    </div>
  </div>
  <div class="form-group">
    <label for="year" class="col-sm-2 control-label">Production Year</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="year" id="year" />
    </div>
  </div>
  <div class="form-group">
    <label for="cd" class="col-sm-2 control-label">CD</label>
    <div class="col-sm-10">
      <select class="form-control" name="cd" id="cd">
        <option value="5678">5678</option>
        <option value="5679">5679</option>
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="singer" class="col-sm-2 control-label">Singer</label>
    <div class="col-sm-10">
      <select class="form-control" name="singer" id="singer">
        <option value="1234">1234</option>
        <option value="1235">1235</option>
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="songwriter" class="col-sm-2 control-label">Songwriter</label>
    <div class="col-sm-10">
      <select class="form-control" name="songwriter" id="songwriter">
        <option value="1234">1234</option>
        <option value="1235">1235</option>
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="composer" class="col-sm-2 control-label">Composer</label>
    <div class="col-sm-10">
      <select class="form-control" name="composer" id="composer">
        <option value="1234">1234</option>
        <option value="1235">1235</option>
      </select>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>
% include('footer.tpl')
