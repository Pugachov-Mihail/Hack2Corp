import 'package:shop_app/domain/model/user.dart';
import 'package:shop_app/domain/model/user_token.dart';

abstract class UserRepository {
  Future<User> getUser({
    required String mail,
    required String password,
  });
}

abstract class UserTokenRepository {
  Future<UserToken> getUserToken({
    required String mail,
    required String password,
  });
}