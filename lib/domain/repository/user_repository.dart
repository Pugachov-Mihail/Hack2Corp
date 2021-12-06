import 'package:shop_app/domain/model/user.dart';

abstract class UserRepository {
  Future<User> getUser({
    required String mail,
    required String password,
  });
}