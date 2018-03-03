module.exports = function(grunt) {
    grunt.initConfig({
        watch: {
            options: {
                livereload: true,
            },
            css: {
                files: ['static/**/*.css', '**/*.html'],
            },
        },
    });

    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['watch']);


};