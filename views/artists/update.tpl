% include('header.tpl')
<h1 class="text-center">Update Artist Information</h1>
<form class="form-horizontal" action="artists/707" method="post">
  <div class="form-group">
    <label for="id" class="col-sm-2 control-label">National ID</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="id" id="id" value="1234"
      disabled="disabled" />
    </div>
  </div>
  <div class="form-group">
    <label for="name" class="col-sm-2 control-label">Name</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="name" id="name"
      value="Tasos" />
    </div>
  </div>
  <div class="form-group">
    <label for="surname" class="col-sm-2 control-label">Surname</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="surname" id="surname"
      value="Karakostas" />
    </div>
  </div>
  <div class="form-group">
    <label for="year" class="col-sm-2 control-label">Birth Year</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="year" id="year"
      value="1978" />
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary">Update Information</button>
    </div>
  </div>
</form>
% include('footer.tpl')
