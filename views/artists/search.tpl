% include('header.tpl')
<h1 class="text-center">Presentation of Artists</h1>
<form class="form-horizontal" action="artists/list" method="post">
  <div class="form-group">
    <label for="name" class="col-sm-2 control-label">Name</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="name" id="name" />
    </div>
  </div>
  <div class="form-group">
    <label for="surname" class="col-sm-2 control-label">Surname</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="surname" id="surname"/>
    </div>
  </div>
  <div class="form-group">
    <label for="yearfrom" class="col-sm-2 control-label">
      Birth Year - From
    </label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="yearfrom" id="yearfrom" />
    </div>
  </div>
  <div class="form-group">
    <label for="yearto" class="col-sm-2 control-label">Birth Year - To</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="yearto" id="yearto" />
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2 control-label">Type</label>
    <div class="col-sm-10">
      <div class="radio">
        <label>
          <input type="radio" name="type" value="singer" checked="checked" />
          Singer
        </label>
      </div>
      <div class="radio">
        <label>
          <input type="radio" name="type" value="songwriter" />
          Songwriter
        </label>
      </div>
      <div class="radio">
        <label>
          <input type="radio" name="type" value="composer" />
          Composer
        </label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>
% include('footer.tpl')
