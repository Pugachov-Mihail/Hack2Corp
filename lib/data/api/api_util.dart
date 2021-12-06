import 'package:shop_app/data/api/request/get_user_body.dart';
import 'package:shop_app/data/api/service/autorization_service.dart';
import 'package:shop_app/data/mapper/UserMapper.dart';
import 'package:shop_app/domain/model/user.dart';

class ApiUtil {
  final AutorizationService _autorizationService;

  ApiUtil(this._autorizationService);

  Future<User> getUser({
    required String? mail,
    required String? password,
  }) async {
    final body = GetUserBody(mail: mail, password: password);
    final result = await _autorizationService.getUser(body);
    return UserMapper.fromApi(result);
  }
}