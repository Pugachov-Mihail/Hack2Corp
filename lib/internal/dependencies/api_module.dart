import 'package:shop_app/data/api/api_util.dart';
import 'package:shop_app/data/api/service/autorization_service.dart';

class ApiModule {
  static ApiUtil? _apiUtil;

  static ApiUtil? apiUtil() {
    if (_apiUtil == null) {
      _apiUtil = ApiUtil(AutorizationService());
    }
    return _apiUtil;
  }
}