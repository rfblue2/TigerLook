Router.configure({ layoutTemplate: 'layout'});

Router.route('/', { 
    name: 'home',
    waitOn: () => {
    },
    loadingTemplate: 'loading'
});
