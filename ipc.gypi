# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'target_defaults': {
    'variables': {
      'ipc_target': 0,
    },
    'target_conditions': [
      # This part is shared between the targets defined below.
      ['ipc_target==1', {
        'sources': [
          'attachment_broker.cc',
          'attachment_broker.h',
          'attachment_broker_messages.h',
          'attachment_broker_privileged.cc',
          'attachment_broker_privileged.h',
          'attachment_broker_privileged_mac.cc',
          'attachment_broker_privileged_mac.h',
          'attachment_broker_privileged_win.cc',
          'attachment_broker_privileged_win.h',
          'attachment_broker_unprivileged.cc',
          'attachment_broker_unprivileged.h',
          'attachment_broker_unprivileged_mac.cc',
          'attachment_broker_unprivileged_mac.h',
          'attachment_broker_unprivileged_win.cc',
          'attachment_broker_unprivileged_win.h',
          'brokerable_attachment.cc',
          'brokerable_attachment.h',
          'brokerable_attachment_mac.cc',
          'brokerable_attachment_win.cc',
          'export_template.h',
          'handle_attachment_win.cc',
          'handle_attachment_win.h',
          'handle_win.cc',
          'handle_win.h',
          'ipc_channel.cc',
          'ipc_channel.h',
          'ipc_channel_factory.cc',
          'ipc_channel_factory.h',
          'ipc_channel_common.cc',
          'ipc_channel_handle.h',
          'ipc_channel_nacl.cc',
          'ipc_channel_nacl.h',
          'ipc_channel_posix.cc',
          'ipc_channel_posix.h',
          'ipc_channel_proxy.cc',
          'ipc_channel_proxy.h',
          'ipc_channel_reader.cc',
          'ipc_channel_reader.h',
          'ipc_channel_win.cc',
          'ipc_channel_win.h',
          'ipc_descriptors.h',
          'ipc_endpoint.cc',
          'ipc_endpoint.h',
          'ipc_export.h',
          'ipc_handle_win.cc',
          'ipc_handle_win.h',
          'ipc_listener.h',
          'ipc_logging.cc',
          'ipc_logging.h',
          'ipc_message.cc',
          'ipc_message.h',
          'ipc_message_attachment.cc',
          'ipc_message_attachment.h',
          'ipc_message_attachment_set.cc',
          'ipc_message_attachment_set.h',
          'ipc_message_generator.cc',
          'ipc_message_generator.h',
          'ipc_message_macros.h',
          'ipc_message_start.h',
          'ipc_message_templates.h',
          'ipc_message_templates_impl.h',
          'ipc_message_utils.cc',
          'ipc_message_utils.h',
          'ipc_param_traits.h',
          'ipc_platform_file.cc',
          'ipc_platform_file.h',
          'ipc_platform_file_attachment_posix.cc',
          'ipc_platform_file_attachment_posix.h',
          'ipc_sender.h',
          'ipc_switches.cc',
          'ipc_switches.h',
          'ipc_sync_channel.cc',
          'ipc_sync_channel.h',
          'ipc_sync_message.cc',
          'ipc_sync_message.h',
          'ipc_sync_message_filter.cc',
          'ipc_sync_message_filter.h',
          'mach_port_attachment_mac.cc',
          'mach_port_attachment_mac.h',
          'mach_port_mac.cc',
          'mach_port_mac.h',
          'message_filter.cc',
          'message_filter.h',
          'message_filter_router.cc',
          'message_filter_router.h',
          'message_router.cc',
          'message_router.h',
          'param_traits_log_macros.h',
          'param_traits_macros.h',
          'param_traits_read_macros.h',
          'param_traits_write_macros.h',
          'placeholder_brokerable_attachment.cc',
          'placeholder_brokerable_attachment.h',
          'struct_constructor_macros.h',
          'struct_destructor_macros.h',
          'unix_domain_socket_util.cc',
          'unix_domain_socket_util.h',
        ],
        'defines': [
          'IPC_IMPLEMENTATION',
        ],
        'include_dirs': [
          '..',
        ],
        'target_conditions': [
          ['>(nacl_untrusted_build)==1', {
            'sources!': [
              'ipc_channel.cc',
              'ipc_channel_posix.cc',
              'unix_domain_socket_util.cc',
            ],
          }],
          ['OS == "win" or OS == "ios"', {
            'sources!': [
              'unix_domain_socket_util.cc',
            ],
          }],
        ],
      }],
    ],
  },
}
