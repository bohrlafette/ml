var gulp = require('gulp');
var concat = require('gulp-concat');
var ngAnnotate = require('gulp-ng-annotate');

var srcJs = ['src/js/app.js', 'src/js/**/*.js'];
var assets = ['src/**/*.html'];

gulp.task('build', function() {
 return gulp.src(srcJs)
    .pipe(ngAnnotate())
    .pipe(concat('all.js'))
    .pipe(gulp.dest('./dist/'));
});

gulp.task("assets", function() {
    return gulp.src(assets)
        .pipe(gulp.dest('./dist/'));
});

gulp.task("watch", function () {
    return gulp.watch(srcJs.concat(assets), ['build', 'assets']);
});

gulp.task("default", ["build", "assets"]);

