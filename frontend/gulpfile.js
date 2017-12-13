var concat = require('gulp-concat');

var srcJs = ['./src/js/*.js']

gulp.task('scripts', function() {
 return gulp.src(srcJs)
   .pipe(concat('all.js'))
   .pipe(gulp.dest('./dist/'));
});