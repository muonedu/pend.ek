'use strict';
// wrapper function that exposes the grunt instance
module.exports = function (grunt) {
    // load all grunt tasks
    require('load-grunt-tasks')(grunt);
    // this is not required but it shows the elapsed time at the end of the grunt task. just do it. :)
    //require('time-grunt')(grunt);

    // initialize the configuration object
    grunt.initConfig({
        // https://github.com/gruntjs/grunt-contrib-watch
        watch: {
            // task target
            html: {
                files: ['templates/app.html','templates/index.html','index.html'],
                options: {
                    livereload: true,
                },
            }
        },
        // https://github.com/gruntjs/grunt-contrib-sass
    });

    // we register the default task which is run with the command `grunt`
    // by setting default you can have multiple task run as the default grunt command.
    // you can also run 'grunt sass' or 'grunt watch' to access the individual task.
    grunt.registerTask('default', ['html']);
};