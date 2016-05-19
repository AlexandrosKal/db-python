% include('header.tpl')
<h1 class="text-center">Insert Artist</h1>
<form class="form-horizontal" action="artists/create" method="post">
  <div class="form-group">
    <label for="id" class="col-sm-2 control-label">National ID</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="id" id="id" />
    </div>
  </div>
  <div class="form-group">
    <label for="name" class="col-sm-2 control-label">Name</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="name" id="name" />
    </div>
  </div>
  <div class="form-group">
    <label for="surname" class="col-sm-2 control-label">Surname</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="surname" id="surname" />
    </div>
  </div>
  <div class="form-group">
    <label for="year" class="col-sm-2 control-label">Birth Year</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="year" id="year" />
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>

% if results.get('success'):
<div class="center-block bg-success text-center">
  Inserted!
</div>
% elif results.get('success') is not None:
<div class="center-block bg-warning text-center">
  Not inserted!
</div>
% end
% include('footer.tpl')
