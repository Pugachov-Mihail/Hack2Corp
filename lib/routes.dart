import 'package:flutter/widgets.dart';
import 'package:shop_app/presentation/screens/complete_profile/complete_profile_screen.dart';
import 'package:shop_app/presentation/screens/forgot_password/forgot_password_screen.dart';

import 'presentation/screens/sign_in/sign_in_screen.dart';
import 'presentation/screens/sign_up/sign_up_screen.dart';


// We use name route
// All our routes will be available here
final Map<String, WidgetBuilder> routes = {
  SignInScreen.routeName: (context) => SignInScreen(),
  SignUpScreen.routeName: (context) => SignUpScreen(),
  ForgotPasswordScreen.routeName: (context) => ForgotPasswordScreen(),
  CompleteProfileScreen.routeName: (context) => CompleteProfileScreen(),
};
