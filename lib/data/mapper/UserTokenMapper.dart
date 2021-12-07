import 'package:shop_app/data/model/api_user_token.dart';
import 'package:shop_app/domain/model/user_token.dart';

class UserTokenMapper {
  static UserToken fromApi(ApiUserToken token) {
      return UserToken(
        token: token.token
      );
    }
}