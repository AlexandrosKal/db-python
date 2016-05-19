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
% for cd in results['cds']:
        <option value="{{cd['cd']}}">{{cd['cd']}}</option>
% end
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="singer" class="col-sm-2 control-label">Singer</label>
    <div class="col-sm-10">
      <select class="form-control" name="singer" id="singer">
% for artist in results['artists']:
        <option value="{{artist['id']}}">{{artist['id']}}</option>
% end
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="songwriter" class="col-sm-2 control-label">Songwriter</label>
    <div class="col-sm-10">
      <select class="form-control" name="songwriter" id="songwriter">
% for artist in results['artists']:
        <option value="{{artist['id']}}">{{artist['id']}}</option>
% end
      </select>
    </div>
  </div>
  <div class="form-group">
    <label for="composer" class="col-sm-2 control-label">Composer</label>
    <div class="col-sm-10">
      <select class="form-control" name="composer" id="composer">
% for artist in results['artists']:
        <option value="{{artist['id']}}">{{artist['id']}}</option>
% end
      </select>
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
