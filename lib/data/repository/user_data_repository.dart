import 'package:shop_app/data/api/api_util.dart';
import 'package:shop_app/domain/model/user.dart';
import 'package:shop_app/domain/model/user_token.dart';
import 'package:shop_app/domain/repository/user_repository.dart';

class UserDataRepository implements UserRepository, UserTokenRepository {
  final ApiUtil _apiUtil;

  UserDataRepository(this._apiUtil);

  @override
  Future<User> getUser({required String mail, required String password}) {
    return _apiUtil.getUser(mail: mail, password: password);
  }

  @override
  Future<UserToken> getUserToken({required String mail, required String password}) {
    return _apiUtil.getToken(mail: mail, password: password);
  }
}