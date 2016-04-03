if (Meteor.isClient) {
    
    // counter starts at 0
    Session.setDefault('counter', 0);
    
    Template.body.helpers({
        faces: [{src:"http://www.princeton.edu/deptafe_internal/cimg!0/dxl1kmtla6gcraqorukj95nrmavdsts"}, 
                {src:"http://www.princeton.edu/deptafe_internal/cimg!0/axtz0nij9jr2qctwcqeq2dauwplreqx"}, 
                {src:"http://www.princeton.edu/deptafe_internal/cimg!0/iuilrhps9y0anb86plua7bbrh7d7jhe"}, 
                {src:"http://www.princeton.edu/deptafe_internal/cimg!0/lsgnytv9w92nzlmq67rhu7y1wv92bj"}, 
                {src:"http://www.princeton.edu/deptafe_internal/cimg!0/ogcys7dc8co5b9ztrhjv4h663yvgsgn"}],
        names: [{name:"Roland"},
                {name:"Casey"},
                {name:"Matthew"},
                {name:"Evan"},
                {name:"Gordon"}]
    });
}

if (Meteor.isServer) {
    Meteor.startup(function () {
        // code to run on server at startup
    });
}
