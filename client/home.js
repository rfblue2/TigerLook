

Template.home.created() = function() {
	face_arr = Session.get("getInitialFaces");
	Session.set("face_arr", face_arr);
};

Template.home.helpers({
    faces: function () { 
				return Session.get("face_arr");
			}
});

Template.home.events({
	'click button'(event, instance) {
		console.log("clicked button");
		Session.get("reset");
		face_arr = Session.get("getInitialFaces");
		Session.set("face_arr", face_arr);
	}
});

Template.face.events({
	'click .clickable_face'(event, instance) {
		console.log(Blaze.getData(event.target)._id);
		var clickedId = Blaze.getData(event.target)._id;
		$( ".clickable_face" ).animate({'opacity' : 0}, function() {
			// get next faces and set them to face_arr
			face_arr = (Session.get("getNextFaces"))(clickedId);
			Session.set("face_arr", face_arr);

			$( ".clickable_face" ).animate({'opacity' : 1});
		});

	}
});