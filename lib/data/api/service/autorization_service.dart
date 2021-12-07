import 'package:dio/dio.dart';
import 'package:shop_app/data/api/request/get_user_token.dart';
import 'package:shop_app/data/model/api_user_token.dart';

class AutorizationService {
  static const _BASE_URL = 'https://2877-185-34-240-5.ngrok.io/api/auth/token/login/';

  final Dio _dio = Dio(
    BaseOptions(baseUrl: _BASE_URL),
  );

  Future<ApiUserToken> getUser(GetUserToken body) async {
    final response = await _dio.get(
      '/json',
      queryParameters: body.toApi(),
    );
    return ApiUserToken.fromApi(response.data);
  }
}