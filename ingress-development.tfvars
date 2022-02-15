dns_base_domain               = "eks.heyvaldemar.net"
ingress_gateway_chart_name    = "nginx-ingress"
ingress_gateway_chart_repo    = "https://helm.nginx.com/stable"
ingress_gateway_chart_version = "0.5.2"
ingress_gateway_annotations = {
  "controller.service.httpPort.targetPort"                                                                    = "http",
  "controller.service.httpsPort.targetPort"                                                                   = "http",
  "controller.service.annotations.service\\.beta\\.kubernetes\\.io/aws-load-balancer-backend-protocol"        = "http",
  "controller.service.annotations.service\\.beta\\.kubernetes\\.io/aws-load-balancer-ssl-ports"               = "https",
  "controller.service.annotations.service\\.beta\\.kubernetes\\.io/aws-load-balancer-connection-idle-timeout" = "60",
  "controller.service.annotations.service\\.beta\\.kubernetes\\.io/aws-load-balancer-type"                    = "elb"
}
