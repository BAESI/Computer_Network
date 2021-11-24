var passport = require('passport');
var GoogleStrategy = require('passport-google-oauth2').Strategy;

passport.use(new GoogleStrategy(
        {
                clientID : '55986542851-s2drdcm0c86p6a2ud8bkn1uv2cv79e2g.apps.googleusercontent.com',
                clientSecret : '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',
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
