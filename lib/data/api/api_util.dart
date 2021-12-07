import 'package:shop_app/data/api/request/get_user_body.dart';
import 'package:shop_app/data/api/request/get_user_token.dart';
import 'package:shop_app/data/mapper/UserMapper.dart';
import 'package:shop_app/data/mapper/UserTokenMapper.dart';
import 'package:shop_app/domain/model/user.dart';
import 'package:shop_app/domain/model/user_token.dart';

import 'service/autorization_service.dart';
import 'service/registration_service.dart';

class ApiUtil {
  final RegistrationService _registrationService;
  final AutorizationService _autorizationService;

  ApiUtil(this._registrationService, this._autorizationService);

  Future<User> getUser({
    required String? mail,
    required String? password,
  }) async {
    final body = GetUserBody(mail: mail, password: password);
    final result = await _registrationService.getUser(body);
    return UserMapper.fromApi(result);
  }

  Future<UserToken> getToken({
    required String? mail,
    required String? password,
  }) async {
    final body = GetUserToken(mail: mail, password: password);
    final result = await _autorizationService.getUser(body);
    return UserTokenMapper.fromApi(result);
  }
}