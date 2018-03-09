module.exports = function(grunt) {
    grunt.initConfig({
        watch: {
            css: {
                files: ['static/**/*.css', 'static/**/*.scss', '**/*.html'],
                options: {
                    livereload: true
                }
            }
        },
        sass: {
            dist: {
                files: {
                    'static/COMPILED/css/custom.css': 'static/css/custom.scss'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('sass', ['watch', 'sass'])


};