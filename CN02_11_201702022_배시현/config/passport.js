var passport = require('passport');
var GoogleStrategy = require('passport-google-oauth2').Strategy;

passport.use(new GoogleStrategy(
        {
                clientID : '',
                clientSecret : '',
		callbackURL : '/auth/google/callback',
		passReqToCallback : true
	}, function(request, accessToken, refreshToken, profile, done) {
	   console.log('profile: ', profile);
	   var user = profile;
	 
	   done(null, user);
	}
));
passport.serializeUser((user, done) => {
	done(null, user);
});
passport.deserializeUser((user, done) => {
	done(null, user);
});

module.exports = passport;
