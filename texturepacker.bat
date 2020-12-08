@ECHO OFF

COLOR A

ECHO -------------------------------------------------------------------------
ECHO                   ** Creating Textures XBT File... **
ECHO -------------------------------------------------------------------------

ECHO.
REM main textures
START /B /WAIT TexturePacker -dupecheck -input media\ -output media\Textures.xbt
REM theme textures
START /B /WAIT TexturePacker -dupecheck -input themes\themename -output media\Themename.xbt
ECHO.

ECHO.
ECHO.

ECHO -------------------------------------------------------------------------
ECHO        ** XBT build complete - scroll up to check for errors. **
ECHO -------------------------------------------------------------------------

PAUSE > NUL