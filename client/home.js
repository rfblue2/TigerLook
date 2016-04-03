face_arr = [{_id:"http://www.princeton.edu/deptafe_internal/cimg!0/dxl1kmtla6gcraqorukj95nrmavdsts", name:"Roland"}, 
            {_id:"http://www.princeton.edu/deptafe_internal/cimg!0/axtz0nij9jr2qctwcqeq2dauwplreqx", name:"Casey"}, 
            {_id:"http://www.princeton.edu/deptafe_internal/cimg!0/iuilrhps9y0anb86plua7bbrh7d7jhe", name:"Matthew"}, 
            {_id:"http://www.princeton.edu/deptafe_internal/cimg!0/lsgnytv9w92nzlmq67rhu7y1wv92bj", name:"Evan"}, 
            {_id:"http://www.princeton.edu/deptafe_internal/cimg!0/ogcys7dc8co5b9ztrhjv4h663yvgsgn", name:"Gordon"}];

Session.set("face_arr", face_arr);

Template.home.helpers({
    faces: function () { 
				return Session.get("face_arr");
			}
});

Template.face.events({
	'click .clickable_face'(event, instance) {
		console.log(Blaze.getData(event.target)._id);
		var testId = Blaze.getData(event.target)._id;
		for (var i = 0; i < face_arr.length; i++) {
			if (testId == face_arr[i]._id) {
				$( ".clickable_face" ).animate({'opacity' : 0}, function() {
					face_arr[i] = {_id:"http://www.princeton.edu/deptafe_internal/cimg!0/ogcys7dc8co5b9ztrhjv4h663yvgsgn", name:"Gordon"};
					Session.set("face_arr", face_arr);
					$( ".clickable_face" ).animate({'opacity' : 1});
				});
				
				break;
			}
		}

	}
});