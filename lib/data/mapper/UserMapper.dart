import 'package:shop_app/data/model/api_user.dart.dart';
import 'package:shop_app/domain/model/user.dart';

class UserMapper {
  static User fromApi(ApiUser user) {
    return User(
      name: user.name,
      surname: user.surname,
      password: user.password,
      mail: user.mail,
    );
  }
}
