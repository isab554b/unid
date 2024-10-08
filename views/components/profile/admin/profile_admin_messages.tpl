<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_messages"]["decorative_header_text"]}}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_messages"]["header_text"]}}
    </h2>
  </div>
  <div class="grid gap-8">
    <!-- prettier-ignore -->
    % if messages: 
      % for message in messages:
    <div class="message-block">
      <div id="content_box_styling">
        <div
          id="content_box_header_styling"
          class="space-y-1 lg:space-y-0 lg:flex justify-between"
        >
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="text-unidDarkBlue">
              % include(global_content['ui_icons']['message'])
            </div>
            <p id="content_box_header_text">{{ message["message_subject"] }}</p>
          </div>
          <p>Sendt den: {{ message["formatted_created_at"] }}</p>
        </div>
        <div class="flex flex-col gap-8 p-6 text-unidDarkBlue">
          <div class="space-y-8 text-sm">
            <div class="space-y-2 text-sm">
              <div class="space-y-1">
                <div
                  class="lg:flex space-y-1 lg:space-y-0 justify-between items-center"
                >
                  <div class="flex gap-2 items-center">
                    <p id="form_label">Afsender:</p>
                    <p class="text-base font-medium">
                      {{ message["first_name"] }} {{ message["last_name"] }}
                    </p>
                  </div>
                  <p class="font-medium">
                    {{ message["website_name"] }}:
                    {{ message["website_url"] }}
                  </p>
                </div>
                <hr />
              </div>
              <div class="space-y-2">
                <div class="flex gap-2">
                  <p class="font-semibold">Emne:</p>
                  <p>{{ message["message_subject"] }}</p>
                </div>
                <div class="lg:flex gap-2">
                  <p class="font-semibold">Besked:</p>
                  <p>{{ message["message_text"] }}</p>
                </div>
              </div>
            </div>
            <div class="w-full flex justify-between">
              <div>
                % if message['message_file']:
                <a
                  class="group transition duration-300 cursor-pointer text-unidLightBlue text-sm hover:scale-105 font-semibold ease-in-out"
                  href="{{ message['message_file'] }}"
                  target="_blank"
                >
                  <div class="flex gap-1.5">
                    <div id="icon_small">
                      % include(global_content['ui_icons']['documents'])
                    </div>
                    <div>
                      <p>Se vedhæftede filer</p>
                      <span
                        class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-unidDarkBlue"
                      ></span>
                    </div>
                  </div>
                </a>
                % end
              </div>
              <div class="text-red-600">
                <div class="justify-end flex items-center">
                  <button
                    data-message-id="{{ message['message_id'] }}"
                    onclick="deleteMessage(this)"
                    type="button"
                    class="items-center flex gap-1.5 text-sm font-semibold"
                  >
                    <div id="icon_small">
                      % include(global_content['ui_icons']['trashcan'])
                    </div>
                    Slet
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end 
      % else:
    <p class="text-sm">Ingen beskeder at vise endnu.</p>
    % end
  </div>
</div>
