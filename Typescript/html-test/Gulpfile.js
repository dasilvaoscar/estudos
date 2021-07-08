var gulp = require("gulp");
var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");
var concat = require('gulp-concat');
const stripImportExport = require('gulp-strip-import-export');

gulp.task("compile", async function () {
  return tsProject.src()
    .pipe(stripImportExport())
    .pipe(tsProject())
    .js.pipe(gulp.dest("js"));
})

gulp.task("concat", async function () {
  return gulp.src(['./js/teste1/test.js', './js/main.js'])
    .pipe(concat('all.js'))
    .pipe(gulp.dest('./dist/'))
});
