import 'package:shop_app/data/api/api_util.dart';
import 'package:shop_app/domain/model/user.dart';
import 'package:shop_app/domain/repository/user_repository.dart';

class UserDataRepository extends UserRepository {
  final ApiUtil _apiUtil;

  UserDataRepository(this._apiUtil);

  @override
  Future<User> getUser({String? mail, String? password}) {
    return _apiUtil.getUser(mail: mail, password: password);
  }
}